from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6e25b49d-44f1-5e6a-a950-b433f8399d51',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Yveltal.Name',
    display_name='Yveltal',
    searchable_by=['Yveltal', 'Basic', 'Yveltal'],
    subtypes=['Basic'],
    collector_number=118,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=717,
    abilities=[
        Attack(
            title='Cross-Cut',
            game_text="If your opponent's Active Pokémon is an Evolution Pokémon, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Dark Edge',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
