from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='729d4c52-67e8-5cbd-95ee-521f14c8505b',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name',
    display_name='Jirachi ◇',
    searchable_by=['Jirachi ◇', 'Basic', 'Prism Star', 'Jirachi'],
    subtypes=['Basic', 'Prism Star'],
    collector_number=97,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Prism,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=385,
    abilities=[
        Ability(
            title='Wish Upon a Star',
            game_text="If you took this Pokémon as a face-down Prize card during your turn and your Bench isn't full, before you put it into your hand, you may put it onto your Bench and take 1 more Prize card.",
            passive=standard_passive("If you took this Pokémon as a face-down Prize card during your turn and your Bench isn't full, before you put it into your hand, you may put it onto your Bench and take 1 more Prize card."),
        ),
        Attack(
            title='Perish Dream',
            game_text="This Pokémon is now Asleep. At the end of your opponent's next turn, the Defending Pokémon will be Knocked Out.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
