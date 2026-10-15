class LimSystem{
    constructor(end,length,speed,creature){
        this.creature = creature;
        this.node = [];
        for(var i = 0; i< length; i++){
            this.node.unshift(node);
            node = node.parent;
            if (!node,isSegment){
                this.length = i + 1;
                break;
            }
        }
        this.hip = this.nodes[0].parent;
    }
    update(){
        this.moveTo(Input.mouse.x, Input.mouse.y)
    }
}