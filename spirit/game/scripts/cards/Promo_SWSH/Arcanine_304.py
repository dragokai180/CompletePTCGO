from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a112cc6d-8c1e-5daf-9b05-c5b82864e2d6',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name',
    display_name='Arcanine',
    searchable_by=['Arcanine', 'Stage 1', 'Arcanine'],
    subtypes=['Stage 1'],
    collector_number=304,
    set_code='Promo_SWSH',
    regulation_mark='F',
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    attributes={200790: {'type': 'string', 'value': 'SWSH304'}},
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name',
    family_id=58,
    abilities=[
        Attack(
            title='Sun-Drenched Tackle',
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
