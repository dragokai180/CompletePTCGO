from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='aa433ae1-3806-57c5-9059-fde258384956',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.LuxrayBREAK.Name',
    display_name='Luxray BREAK',
    searchable_by=['Luxray BREAK', 'BREAK', 'LuxrayBREAK'],
    subtypes=['BREAK'],
    collector_number=47,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.BreakRare,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Luxray.Name',
    family_id=403,
    abilities=[
        Attack(
            title='Wild Fury',
            game_text='Flip a coin until you get tails. This attack does 40 more damage for each heads.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
