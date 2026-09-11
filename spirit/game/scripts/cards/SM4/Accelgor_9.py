from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c530de71-fbff-5f12-bd08-4654d5a873c1',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Accelgor.Name',
    display_name='Accelgor',
    searchable_by=['Accelgor', 'Stage 1', 'Accelgor'],
    subtypes=['Stage 1'],
    collector_number=9,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shelmet.Name',
    family_id=616,
    abilities=[
        Attack(
            title='Recover',
            game_text='Discard an Energy from this Pokémon and heal all damage from it.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Speed Attack',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
