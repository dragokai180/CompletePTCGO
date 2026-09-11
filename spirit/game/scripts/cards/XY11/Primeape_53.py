from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4aac6493-4980-51bc-aec9-86d2c5ca7d99',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name',
    display_name='Primeape',
    searchable_by=['Primeape', 'Stage 1', 'Primeape'],
    subtypes=['Stage 1'],
    collector_number=53,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name',
    family_id=56,
    abilities=[
        Attack(
            title='Swagger',
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Spirited Throw',
            game_text="If, before doing damage, your opponent's Active Pokémon has more remaining HP than this Pokémon, this attack does 60 more damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
