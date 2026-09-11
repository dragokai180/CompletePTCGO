from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='35e9327a-fe1f-5907-b82c-2f8edf6b7578',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.DelphoxBREAK.Name',
    display_name='Delphox BREAK',
    searchable_by=['Delphox BREAK', 'BREAK', 'DelphoxBREAK'],
    subtypes=['BREAK'],
    collector_number=14,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.BreakRare,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Delphox.Name',
    family_id=653,
    abilities=[
        Ability(
            title='Flare Witch',
            game_text='Once during your turn (before your attack), you may search your deck for a Fire Energy card and attach it to 1 of your Pokémon. Shuffle your deck afterward.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
    ],
)
