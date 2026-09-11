from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='90305c28-cb00-556f-a45a-15b4ebbf3832',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name',
    display_name='Zubat',
    searchable_by=['Zubat', 'Basic', 'Zubat'],
    subtypes=['Basic'],
    collector_number=110,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=41,
    abilities=[
        Attack(
            title='Supersonic',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Razor Wing',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
