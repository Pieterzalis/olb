  theme_minimal() + 
  theme(panel.grid.minor = element_blank(),
        panel.grid.major.x = element_blank(),
        panel.grid.major.y = element_blank(),
        axis.ticks.length = unit(0, "cm"),
        text=element_text(family='Arial'),
        plot.title = element_text(size=16,hjust=0.0,face='bold'),
        plot.subtitle = element_text(size=14,face='italic'),
        axis.text.x = element_text(size=16,color="black",face='bold'),
        legend.position="top",
        legend.title = element_blank(),
        legend.text = element_text(color = "black", size = 14,face='bold'),
        axis.text.y = element_blank(),
        axis.title.x = element_text(color="black", size=14),
        axis.title.y = element_text(color="black", size=14)) +
  scale_y_continuous(limits=c(-0,1700),breaks=c(500,1000,1500),expand=c(0.0,0))
