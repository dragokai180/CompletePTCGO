from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d2e050d2-0fc4-55f8-8d07-5c657d68748c',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name',
    display_name='Braixen',
    searchable_by=['Braixen', 'Stage 1', 'Braixen'],
    subtypes=['Stage 1'],
    collector_number=16,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Fennekin.Name',
    family_id=653,
    abilities=[
        Attack(
            title='Flare',
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title='Flamethrower',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
