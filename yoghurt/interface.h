#ifndef __INTERFACE_H__
#define __INTERFACE_H__

const double EPS = 1e-9;

// TODO: ��ʵ���ǲ�̫���������涼��ɶ��˼
enum WAY_OF_DAY_COUNT {
    GERMAN = 1,
    SPECIAL_GERMAN = 2,
    // TODO: ����/���������������ֿ�ͷ
    // 30U_360 = 3,
    U30_360 = 3,
    ACT_ACT = 4,
    ACT_360 = 5,
    ACT_365 = 6,
};

struct bond_content  
{
    double face;
    double coupon;
    double maturity;

    // �������㷽��, �� WAY_OF_DAY_COUNT
    int way_of_day_count;

    // TODO: ����ɶ? �� get_value_date ��������ֵ, �ֱ�ָ��ʲô?
    int frequence;

    //   1: һ����������ծȯ
    //   2: һ���Ի�����Ϣծȯ����Ϣծȯ
    //   3: �̶����ʸ�Ϣծȯ,
    int type;
};

#endif

