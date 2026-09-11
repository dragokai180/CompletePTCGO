from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='88f12191-6c32-5cc2-84e0-2a9fba3c0f24',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name',
    display_name='Baltoy',
    searchable_by=['Baltoy', 'Basic', 'Baltoy'],
    subtypes=['Basic'],
    collector_number=78,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=343,
    abilities=[
        Attack(
            title='Psy Bolt',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
