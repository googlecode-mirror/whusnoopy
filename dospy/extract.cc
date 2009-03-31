#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <iconv.h>

const int MAX_PAGE_LENGTH = 1048576; // 1M per page
const int MAX_FILE_NAME = 128;

int printUsage() {
  printf("Usage:\n");
  printf("  exDospy filename\n");
  return 0;
}

int gbk2utf8(char* in_str, char* out_str) {
  iconv_t cd = iconv_open("utf-8", "gbk");
  if (cd == 0)
    return -1;

  size_t instrlen = strlen(in_str);
  size_t outstrlen = MAX_PAGE_LENGTH;
  if (iconv(cd, &in_str, &instrlen, &out_str, &outstrlen) == -1)
    return -2;
  
  iconv_close(cd);
  return 0;
}

int grepQuote(char* str) {
  char *tp;
  char *rp;
  while (tp = strstr(str, "<div class=\"msgbody\"><div class=\"msgheader\">")) {
    rp = strstr(tp, "</div></div>") + 12;
    if (*rp == '\0') {
      *tp = '\0';
    } else {
      strncpy(tp, rp, strlen(rp) + 1);
    }
  }

  return 0;
}

int grepHtmlTag(char* str) {
  char *tp;
  char *rp;

  while (tp = strstr(str, "<")) {
    if (tp >= str + strlen(str))
      break;

    rp = strstr(tp, ">") + 1;

    if (*rp == '\0') {
      *tp = '\0';
    } else {
      strncpy(tp, rp, strlen(rp) + 1);
    }
  }

  return 0;
}

int convertHtmlChar(char* str) {
  char html_code[5][2][8] = {
    "&nbsp;", " ",
    "&amp;", "&",
    "&lt;", "<",
    "&gt;", ">",
    "&quot;", "\""
  };
  char* tp;

  for (int i = 0; i < 5; ++i) {
    int len = strlen(html_code[i][0]) - 1;
    while (tp = strstr(str, html_code[i][0])) {
      strncpy(tp, tp + len, strlen(tp + len));
      *tp = html_code[i][1][0];
    }
  }

  return 0;
}

int main(int argc, char* argv[]) {
  char target_file_name[MAX_FILE_NAME + 1];
  char buf[MAX_PAGE_LENGTH + 1];
  char page_content[MAX_PAGE_LENGTH + 1];
  char title[MAX_PAGE_LENGTH + 1];

  if (argc < 2 ) {
    printUsage();
    exit(0);
  } else if (argc < 3) {
    time_t t = time(NULL);
    struct tm tm;
    localtime_r(&t, &tm);
    strftime(target_file_name, MAX_FILE_NAME, "%Y%m%d-%H%M%S", &tm);
  } else {
    strncpy(target_file_name, argv[2], MAX_FILE_NAME);
  }

  int offset = strlen(target_file_name) + 1;
  strcat(target_file_name, ".0000");

  FILE* origin_file = fopen(argv[1], "r");
  memset(page_content, 0, sizeof(page_content));
  memset(buf, 0, sizeof(buf));

  while (!feof(origin_file)) {
    fgets(buf, MAX_PAGE_LENGTH, origin_file);
    strncat(page_content, buf, MAX_PAGE_LENGTH);
  }
  gbk2utf8(page_content, buf);
  strncpy(page_content, buf, MAX_PAGE_LENGTH);

  char* sp;
  char* tp;

  // detect title
  sp = strstr(page_content, "<title>");
  sp += 7;
  tp = strstr(sp, "-");
  strncpy(title, sp, tp - sp);
  title[tp - sp - 1] = '\0';

  FILE* target_file;
  int target_file_no = 0;

  while (sp = strstr(sp, "<div style=\"padding-top: 4px;\">")) {
    target_file_no++;
    sprintf(&target_file_name[offset], "%04d", target_file_no);
    target_file = fopen(target_file_name, "w");
    char date_time[MAX_PAGE_LENGTH + 1];
    char content[MAX_PAGE_LENGTH + 1];
    
    // detect date time info
    sp += 42;
    tp = strstr(sp, "&nbsp");
    strncpy(buf, sp, tp - sp);
    buf[tp - sp] = '\0';
    strncpy(date_time, buf, strlen(buf) + 1);

    // detect text
    sp = strstr(sp, "class=\"t_msgfont\">");
    sp += 18;
    tp = strstr(sp, "</div>\r\n");
    memset(buf, 0, sizeof(buf));
    strncpy(buf, sp, tp - sp);
    buf[tp - sp] = '\0';

    grepQuote(buf);
    grepHtmlTag(buf);
    convertHtmlChar(buf);
    strncpy(content, buf, strlen(buf) + 1);

    fprintf(target_file, "\n<DOC>\n");
    fprintf(target_file, "<DOCNO> %s </DOCNO>\n", target_file_name);
    fprintf(target_file, "<DATE_TIME> %s </DATE_TIME>\n", date_time);
    fprintf(target_file, "<BODY>\n");
    fprintf(target_file, "<CATEGORY> cellphone </CATEGORY>\n");
    fprintf(target_file, "<HEADLINE> %s </HEADLINE>\n", title);
    fprintf(target_file, "<TEXT>\n");
    fprintf(target_file, "%s\n", content);
    fprintf(target_file, "</TEXT>\n");
    fprintf(target_file, "</BODY>\n");
    fprintf(target_file, "</DOC>\n");
    fclose(target_file);
  }

  return 0;
}

