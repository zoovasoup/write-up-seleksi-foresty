# Baby Reveng
**Author:** BbayuGt

**Difficulty:** easy

---
## Description
This program is cute and simple. It just prints some random numbers. Can you find the flag?

## Enumeration
dikasih file... langsung ada buka pake ghidra.... isinya main..
```

undefined8 main(void)

{
  ostream *this;
  long in_FS_OFFSET;
  uint local_9c;
  int local_98 [34];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_98[0] = 0x46;
  local_98[1] = 0x4f;
  local_98[2] = 0x52;
  local_98[3] = 0x45;
  local_98[4] = 0x53;
  local_98[5] = 0x54;
  local_98[6] = 0x59;
  local_98[7] = 0x7b;
  local_98[8] = 0x62;
  local_98[9] = 0x34;
  local_98[10] = 0x62;
  local_98[0xb] = 0x79;
  local_98[0xc] = 0x5f;
  local_98[0xd] = 0x72;
  local_98[0xe] = 0x33;
  local_98[0xf] = 0x76;
  local_98[0x10] = 0x33;
  local_98[0x11] = 0x6e;
  local_98[0x12] = 0x67;
  local_98[0x13] = 0x3f;
  local_98[0x14] = 0x21;
  local_98[0x15] = 0x5f;
  local_98[0x16] = 0x74;
  local_98[0x17] = 0x65;
  local_98[0x18] = 0x68;
  local_98[0x19] = 0x65;
  local_98[0x1a] = 0x68;
  local_98[0x1b] = 0x65;
  local_98[0x1c] = 0x68;
  local_98[0x1d] = 0x65;
  local_98[0x1e] = 0x3a;
  local_98[0x1f] = 0x33;
  local_98[0x20] = 0x7d;
  for (local_9c = 0; local_9c < 0x21; local_9c = local_9c + 1) {
    this = (ostream *)
           std::ostream::operator<<((ostream *)std::cout,local_98[(int)local_9c] + local_9c);
    std::ostream::operator<<(this,std::endl<>);
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```

keliatan ada array terus arraynya ter assign... 

minta Ai buat baca nilai hexnya 

| index | nilai Hex | ascii|
|--- | --- | --- | 
| 0 | 0x46 | 'F' |
| 1 | 0x4F | 'O' |
| 2 | 0x52 | 'R' |
| 3 | 0x45 | 'E' |
| 4 | 0x53 | 'S' |
| 5 | 0x54 | 'T' |
| 6 | 0x59 | 'Y' |
| 7 | 0x7b | '{' |
| ... | ... | '...' |
| 32 | 0x7d | '}' |



## Flag 
```
FORESTY{b4by_r3v33ng?!_tehehehe:3}
```
