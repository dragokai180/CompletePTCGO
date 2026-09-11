from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='206a292e-3816-5310-98a9-a2cbd44fcfae',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MMewtwoEX.Name',
    display_name='M Mewtwo-EX',
    searchable_by=['M Mewtwo-EX', 'MEGA', 'EX', 'MMewtwoEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=63,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoEX.Name',
    family_id=150,
    abilities=[
        Attack(
            title='Vanishing Strike',
            game_text="If there is any Stadium card in play, this attack does 50 more damage, and this attack's damage isn't affected by Resistance or any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
