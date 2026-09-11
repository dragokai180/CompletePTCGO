from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='49e98d1b-09ec-57da-8cf6-cae40a4029be',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Aromatisse.Name',
    display_name='Aromatisse',
    searchable_by=['Aromatisse', 'Stage 1', 'Aromatisse'],
    subtypes=['Stage 1'],
    collector_number=106,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spritzee.Name',
    family_id=682,
    abilities=[
        Attack(
            title='Heavy Perfume',
            game_text="Your opponent's Active Pokémon is now Confused. Put 6 damage counters instead of 3 on that Pokémon for this Special Condition.",
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Hug',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FAIRY: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
