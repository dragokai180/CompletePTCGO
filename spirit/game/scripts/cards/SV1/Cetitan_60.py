from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8d24de3c-258a-50d9-96c6-62ce2bcdc02d',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cetitan.Name',
    display_name='Cetitan',
    searchable_by=['Cetitan', 'Stage 1', 'Cetitan'],
    subtypes=['Stage 1'],
    collector_number=60,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cetoddle.Name',
    family_id=974,
    abilities=[
        Attack(
            title='Hammer In',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title='Sweeping Tackle',
            game_text='This attack does 20 less damage for each damage counter on this Pokémon.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
            damage_operator='-',
            effect=standard_attack,
        ),
    ],
)
