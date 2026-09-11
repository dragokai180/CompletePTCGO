from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='078d4ad4-5dd0-5174-87b0-7a6be0b234b8',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TalonflameBREAK.Name',
    display_name='Talonflame BREAK',
    searchable_by=['Talonflame BREAK', 'BREAK', 'TalonflameBREAK'],
    subtypes=['BREAK'],
    collector_number=21,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.BreakRare,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Talonflame.Name',
    family_id=661,
    abilities=[
        Attack(
            title='Flare Blitz',
            game_text='Discard all Fire Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 2},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
