from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='94173933-06b5-53d5-9965-d35904c34537',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name',
    display_name='Sableye',
    searchable_by=['Sableye', 'Basic', 'Sableye'],
    subtypes=['Basic'],
    collector_number=133,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=302,
    abilities=[
        Attack(
            title='Mirror Gem',
            game_text="During your opponent's next turn, if this Pokémon is damaged by an attack (even if it is Knocked Out), put 8 damage counters on the Attacking Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
