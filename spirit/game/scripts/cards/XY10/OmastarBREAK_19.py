from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a1f6e027-6fc0-53d3-baa7-28bc29f5ca4f',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.OmastarBREAK.Name',
    display_name='Omastar BREAK',
    searchable_by=['Omastar BREAK', 'BREAK', 'OmastarBREAK'],
    subtypes=['BREAK'],
    collector_number=19,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.BreakRare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Omastar.Name',
    family_id=138,
    abilities=[
        Ability(
            title='Dangerous Tentacle',
            game_text="Once during your turn (before your attack), you may switch 1 of your opponent's Benched Pokémon-EX with his or her Active Pokémon.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
    ],
)
