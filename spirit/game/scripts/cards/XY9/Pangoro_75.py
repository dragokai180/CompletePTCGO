from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f09ad9a7-6c9b-5925-8384-eb4849eb5558',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pangoro.Name',
    display_name='Pangoro',
    searchable_by=['Pangoro', 'Stage 1', 'Pangoro'],
    subtypes=['Stage 1'],
    collector_number=75,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name',
    family_id=674,
    abilities=[
        Attack(
            title='Parting Shot',
            game_text="Switch this Pokémon with 1 of your Benched Pokémon. During your opponent's next turn, any damage done by attacks from the Defending Pokémon is reduced by 60 (before applying Weakness and Resistance).",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Buster Swing',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
