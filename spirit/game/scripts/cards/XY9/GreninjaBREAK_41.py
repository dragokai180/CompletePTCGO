from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
    giant_water_shuriken, giant_water_shuriken_condition,
)


card = PokemonCardDef(
    guid='524342c2-6ed5-5564-8a1c-99790c2209e4',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GreninjaBREAK.Name',
    display_name='Greninja BREAK',
    searchable_by=['Greninja BREAK', 'BREAK', 'GreninjaBREAK'],
    subtypes=['BREAK'],
    collector_number=41,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.BreakRare,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Greninja.Name',
    family_id=656,
    abilities=[
        Ability(
            title='Giant Water Shuriken',
            game_text="Once during your turn (before your attack), if this Pokémon is your Active Pokémon, you may discard a Water Energy card from your hand. If you do, put 6 damage counters on 1 of your opponent's Pokémon.",
            effect=giant_water_shuriken,
            condition=giant_water_shuriken_condition,
            activation=Activations.ONCE_PER_TURN,
        ),
    ],
)
