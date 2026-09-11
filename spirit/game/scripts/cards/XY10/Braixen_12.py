from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e4dfe477-a469-5fbb-aee2-cc576ea0513e',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name',
    display_name='Braixen',
    searchable_by=['Braixen', 'Stage 1', 'Braixen'],
    subtypes=['Stage 1'],
    collector_number=12,
    set_code='XY10',
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
            title='Destructive Flame',
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Crackling Ribbon',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
