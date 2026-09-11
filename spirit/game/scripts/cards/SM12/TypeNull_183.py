from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a49ae1a7-2289-513e-a6e4-1d16e864ed2e',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TypeNull.Name',
    display_name='Type: Null',
    searchable_by=['Type: Null', 'Basic', 'TypeNull'],
    subtypes=['Basic'],
    collector_number=183,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=772,
    abilities=[
        Attack(
            title='Air Slash',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
