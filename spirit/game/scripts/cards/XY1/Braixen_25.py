from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9ff3711c-412c-5a2a-a2c0-394a3d362caa',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name',
    display_name='Braixen',
    searchable_by=['Braixen', 'Stage 1', 'Braixen'],
    subtypes=['Stage 1'],
    collector_number=25,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Fennekin.Name',
    family_id=653,
    abilities=[
        Attack(
            title='Clairvoyant Eye',
            game_text='Look at the top 3 cards of your deck and put them back on top of your deck in any order.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Fire Tail Slap',
            game_text='Discard a Fire Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
