library(mclust)

# MCLUST EXAMPLES APPROACH
pep <- read.table("C:/Users/User/desktop/skinner/out_data/pepALL_N5000_Nrep100.txt")
dat <- pep[,-1]

BIC_pep <- mclustBIC(dat)
plot(BIC_pep)
summary(BIC)

mod <- Mclust(dat, x=BIC_pep)
summary(mod)

write.table(mod$parameters$mean,file="C:/Users/User/desktop/skinner/out_data/clust_out/clust_means.txt")

dat<-numeric()
for (i in 1:length(fit$parameters$pro))
  dat <- cbind(dat,sqrt(diag(fit$parameters$variance$sigma[,,i])))
write.table(file="C:/Users/User/desktop/skinner/out_data/clust_out/clust_var.txt",dat)

#write.table(file="C:/Users/User/desktop/skinner/tmp.var",fit$parameters$variance)
write.table(file="C:/Users/User/desktop/skinner/out_data/clust_out/clust_bic.txt",fit$BIC)
#write.table(file="C:/Users/User/desktop/skinner/clust_out/tmp.z",fit$z)