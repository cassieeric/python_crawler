function char_to_signature(sequence_num){
    string = ""
    for(var i=0; i<24; i+=6){
        nor = sequence_num >> i & 63
        string += fix_str[nor]
    }
    return string
}

function get_signature(md5_str){
    string = ""
    for(var i=32; i>0; i-=3){
        if(i%4===0){
            num_1 = md5_str.charCodeAt(i) ^ 42
        }else{
            num_1 = md5_str.charCodeAt(i)
        }
        if((i-1)%4===0){
            num_2 = (md5_str.charCodeAt(i-1) ^ 42) << 8
        }else{
            num_2 = md5_str.charCodeAt(i-1) << 8
        }
        if((i-2)%4===0){
            num_3 = (md5_str.charCodeAt(i-2) ^ 42) << 16
        }else{
            num_3 = md5_str.charCodeAt(i-2) << 16
        }
        long_number = num_1 | num_2 | num_3
        string += char_to_signature(long_number)
    }
    return string
}

// a_Y0rHe0H92fUCtBML2q6HXyUBFY68S0hwOBbeUqb_xp
fix_str = "RuPtXwxpThIZ0qyz_9fYLCOV8B1mMGKs7UnFHgN3iDaWAJE-Qrk2ecSo6bjd4vl5"
// md5_str = "6d9679eac3f8d6a8c8756d5aa4d3c114\u0000"
// console.log(get_signature(md5_str))


// long_number = (md5_str.charCodeAt(32) ^ 42) | (md5_str.charCodeAt(31) << 8) | (md5_str.charCodeAt(30) << 16)
// console.log(long_number)
// sign_1 = char_to_signature(long_number)
// console.log(sign_1)
// long_number = md5_str.charCodeAt(29) | ((md5_str.charCodeAt(28)^42)<<8) | (md5_str.charCodeAt(27) << 16)
// console.log(long_number)
// sign_2 = char_to_signature(long_number)  // 7733 | 6684672  102<<16=6684672= (md5_str.charCodeAt(27) << 16)  53|7680=7733=(md5_str.charCodeAt(29)| ((md5_str.charCodeAt(28)^42)<<8))
// console.log(sign_2)
// long_number = md5_str.charCodeAt(26) | (md5_str.charCodeAt(25)<<8) | ((md5_str.charCodeAt(24)^42)<<16)
// console.log(long_number)
// sign_3 = char_to_signature(long_number)
// console.log(sign_3)  // 12344|1245184 (r[0]|r[2])   19<<16=1245184 (r[1]|r[2]) 19=57^42 (r[3]^r[1]) (md5_str.charCodeAt(24)^42) // 12344|(md5_str.charCodeAt(24)^42)<<16
// long_number = md5_str.charCodeAt(23) | (md5_str.charCodeAt(22) << 8) | (md5_str.charCodeAt(21) << 16)
// console.log(long_number)
// sign_4 = char_to_signature(long_number) // 6644577  25441|6619136  101<<16=6619136(md5_str.charCodeAt(21) << 16)    97|25344(r[1]|r[3])=25441  99<<8=25344(r[1]<<r[3])
// console.log(sign_4)

// long_number = (md5_str.charCodeAt(20)^ 42) | (md5_str.charCodeAt(19) << 8) | (md5_str.charCodeAt(18) << 16)
// console.log(long_number)
// sign_4 = char_to_signature(long_number) 
// console.log(sign_4)

// long_number = md5_str.charCodeAt(17) | ((md5_str.charCodeAt(16)^42)<<8) | (md5_str.charCodeAt(15) << 16)
// console.log(long_number)
// sign_4 = char_to_signature(4731698) 
// console.log(sign_4)


// 


//  4994358>>>18  = 19  "RuPtXwxpThIZ0qyz_9fYLCOV8B1mMGKs7UnFHgN3iDaWAJE-Qrk2ecSo6bjd4vl5"[19] "Y"

/* 字符串推导 */
// 索引： 346  值：  是第1个字符   (3629866>> 0) & 63  "RuPtXwxpThIZ0qyz_9fYLCOV8B1mMGKs7UnFHgN3iDaWAJE-Qrk2ecSo6bjd4vl5"[33]
// 索引： 357  值：  是第2个字符   (3629866>> 6) & 63
// 索引： 369  值：  是第3个字符   (3629866>> 12) & 63
// 索引： 381  值：  是第4个字符   (3629866>> 18) & 63


function char_to_signature(sequence_num){
    string = ""
    for(var i=0; i<24; i+=6){
        nor = sequence_num >> i & 63
        string += fix_str[nor]
    }
    return string
}

console.log(char_to_signature(6690865))


/* 长数字生成 */
// long_number = (md5_str.charCodeAt(32) ^ 42) | (md5_str.charCodeAt(31) << 8) | (md5_str.charCodeAt(30) << 16)
// 索引： 342  值： 25386|3604480  r[0] | r[2]  = 3629866

// 索引： 341  值： 生成r[2]  55<<16  r[1] << r[2] = 3604480
// 索引： 337  值： 生成r[2].r[1]  "2f4563d1e80175ea4ab6e0b475c98d7c\u0000".charCodeAt(30) == 55   md5_str.charCodeAt(30)

// 索引： 311  值： 生成r[0]  42 |25344     r[0] | r[2]  = 25386
// 索引： 310  值： 生成r[0].r[2]  99<<8     r[1] << r[2] = 25344   md5_str.charCodeAt(31) << 8)
// 索引： 280  值： 生成r[0].r[0] 0^42  r[3]^ r[0] = 42 (md5_str.charCodeAt(32) ^ 42)

// 42 | (md5_str.charCodeAt(31) << 8) | (md5_str.charCodeAt(30) << 16)




// 索引： 342  值： 4994358 = 13622 | 4980736  r[0] | r[2]     md5_str.charCodeAt(31) << 8) |  r[2] 
// 索引： 311  值   r[0]  = ?13622 =     54 | 13568   r[0] | r[2]  
// 索引： 310  值 r[0].r[2] ? = 13568 =  53<<8  r[1] << r[2]  md5_str.charCodeAt(31) << 8)

// 索引： 341  值：r[2]  4980736 = 76<<16  r[1] << r[2]

//  r[2].r[1]


function get_signature(md5_str){
    string = ""
    for(var i=32; i>0; i-=3){
        if(i%4===0){
            num_1 = md5_str.charCodeAt(i) ^ 42
        }else{
            num_1 = md5_str.charCodeAt(i)
        }
        if((i-1)%4===0){
            num_2 = (md5_str.charCodeAt(i-1) ^ 42) << 8
        }else{
            num_2 = md5_str.charCodeAt(i-1) << 8
        }
        if((i-2)%4===0){
            num_3 = (md5_str.charCodeAt(i-2) ^ 42) << 16
        }else{
            num_3 = md5_str.charCodeAt(i-2) << 16
        }
        long_number = num_1 | num_2 | num_3
        string += char_to_signature(long_number)
    }
    return string
}