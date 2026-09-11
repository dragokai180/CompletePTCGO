from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3e8b309d-5687-553e-bb7b-d1f7d55149fa',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.CarbinkBREAK.Name',
    display_name='Carbink BREAK',
    searchable_by=['Carbink BREAK', 'BREAK', 'CarbinkBREAK'],
    subtypes=['BREAK'],
    collector_number=51,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.BreakRare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Carbink.Name',
    family_id=703,
    abilities=[
        Attack(
            title='Diamond Gift',
            game_text='Attach 2 Energy cards from your discard pile to 1 of your Fighting Pokémon.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
