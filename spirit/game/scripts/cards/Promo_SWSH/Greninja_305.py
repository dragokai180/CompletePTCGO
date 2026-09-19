from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7e6fc35f-932f-5062-9ffb-765aa72e5ff1',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Greninja.Name',
    display_name='Greninja',
    searchable_by=['Greninja', 'Stage 2', 'Greninja'],
    subtypes=['Stage 2'],
    collector_number=305,
    set_code='Promo_SWSH',
    regulation_mark='F',
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH305'}},
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name',
    family_id=656,
    abilities=[
        Attack(
            title='Coordinated Shuriken',
            game_text="This attack also does 10 damage to 3 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
