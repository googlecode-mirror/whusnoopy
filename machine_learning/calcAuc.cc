// Copyright 2011 yewen

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdarg.h>
#include <time.h>
#include <math.h>

enum LOG_LEVEL {
    FATA = 0,
    WARN = 1,
    INFO = 2,
    DEBUG = 3,
};
char log_str[4][9] = {
    "FATA",
    "WARN",
    "INFO",
    "DEBUG",
};
int debug_mode;

const int MAX_LINE_LEN = 1024000;

const int MAX_FEA_NUM = 10000000;
double mod_fea[MAX_FEA_NUM];

const int MAX_INS_NUM = 10000000;
struct ins_node {
    int num;
    double weight;
    double prob;
};
ins_node ins_res[MAX_INS_NUM];
int ins_num;

void LOG(int level, const char* format, ...) {
    if (level >= DEBUG && debug_mode == 0) {
        return;
    }

    char buffer[102400];
    int pos = 0;

    // add time
    time_t t = time(NULL);
    struct tm tm;
    localtime_r(&t, &tm);
    char buf[1024];
    strftime(buf, sizeof(buf), "%H:%M:%S", &tm);
    pos += sprintf(&buffer[pos], "%s ", buf);

    // add level
    pos += sprintf(&buffer[pos], "[%s] ", log_str[level]);

    // add logger
    va_list args;
    va_start(args, format);
    vsprintf(&buffer[pos], format, args);
    va_end(args);

    fprintf(stdout, "%s\n", buffer);

    return;
}

void Usage() {
    fprintf(stderr, "Usage: ./calc_auc instance_filename model_filename\n");
    return;
}

char* getToken(char* &buf, const char split_char = '\t') {
    char* ret = buf;
    while (*buf != '\0' && *buf != '\n' && *buf != split_char) {
        buf++;
    }
    *buf = '\0';
    buf++;
    return ret;
}

int loadModel(FILE* fp) {
    char buf[MAX_LINE_LEN] = {0};
    unsigned int id = 0LL;
    double weight = 0;

    while (NULL != fgets(buf, MAX_LINE_LEN, fp)) {
        char* cp = buf;

        char* token = getToken(cp);
        if (1 != sscanf(token, "%u", &id)) {
            return -1;
        }

        token = getToken(cp);
        if (1 != sscanf(token, "%lf", &weight)) {
            return -1;
        }
        mod_fea[id] = weight;
    }

    LOG(DEBUG, "load [%u] feature weight", id);
    for (int i = 1; i <= id; ++i) {
        LOG(DEBUG, "fea[%d] -> %lf", i, mod_fea[i]);
    }

    return 0;
}

double logTrans(double weight) {
    return (1.0 / (1 + exp(-weight)));
}

int loadInstance(FILE* fp) {
    char buf[MAX_LINE_LEN] = {0};
    int num = 0;
    int fea_id = 0;

    ins_num = 0;
    while (NULL != fgets(buf, MAX_LINE_LEN, fp)) {
        char* cp = buf;

        char* token = getToken(cp);
        if (1 != sscanf(token, "%u", &num)) {
            return -1;
        }
        ins_res[ins_num].num = num;
        ins_res[ins_num].weight = 0;

        while (*(token = getToken(cp)) != '\0') {
            if (1 != sscanf(token, "%u", &fea_id)) {
                return -1;
            }
            ins_res[ins_num].weight += mod_fea[fea_id];
            LOG(DEBUG, "ins [%d] has feature [%d] with weight [%f], "
                    "and sum weight of ins [%d] is [%f] now",
                    ins_num, fea_id, mod_fea[fea_id],
                    ins_num, ins_res[ins_num].weight);
        }
        ins_res[ins_num].prob = logTrans(ins_res[ins_num].weight);

        ++ins_num;
    }

    return 0;
}

int cmp(const void *a, const void *b)
{
     ins_node *aa = (ins_node *)a;
     ins_node *bb = (ins_node *)b;
     return(((aa->prob)-(bb->prob)>0)?1:-1);
}

double calcAuc() {
    double res = 0;

    qsort(ins_res, ins_num, sizeof(ins_node), cmp);

    double sum_pos = 0;
    double sum_neg = 0;
    double s0 = 0;
    int count = 0;
    for (int i = 0; i < ins_num; ++i) {
        LOG(DEBUG, "ins [%d] -> num [%d], weight [%f], prob [%f]",
                i, ins_res[i].num, ins_res[i].weight, ins_res[i].prob);
        int this_num = abs(ins_res[i].num);
        if (ins_res[i].num < 0) {
            sum_neg += this_num;
        } else {
            sum_pos += this_num;
            s0 += ((count + 1) + (count + this_num)) * this_num / 2;
        }

        count += this_num;
        LOG(DEBUG, "s0 [%lf] sum_pos [%lf] sum_neg [%lf]", s0, sum_pos, sum_neg);
    }

    res = (s0 - (sum_pos*(sum_pos+1))/2.0)/(sum_pos*sum_neg);

    return res;
}

int main(int argc, char* argv[]) {
    if (argc < 3) {
        Usage();
        return -1;
    } else if (argc > 3) {
        debug_mode = 1;
    } else {
        debug_mode = 0;
    }

    FILE* mod_fp = fopen(argv[1], "r");
    if (NULL == mod_fp) {
        Usage();
        return -2;
    }
    if (0 != loadModel(mod_fp)) {
        Usage();
        fclose(mod_fp);
        return -2;
    }
    fclose(mod_fp);

    FILE* ins_fp = fopen(argv[2], "r");
    if (NULL == ins_fp) {
        Usage();
        return -2;
    }
    if (0 != loadInstance(ins_fp)) {
        Usage();
        fclose(ins_fp);
        return -3;
    }
    fclose(ins_fp);

    double auc_res = 0;
    auc_res = calcAuc();
    LOG(INFO, "Calc auc by model [%s] to instance [%s]: %lf", argv[1], argv[2], auc_res);

    return 0;
}


