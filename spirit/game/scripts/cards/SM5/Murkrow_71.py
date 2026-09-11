from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9801ec82-9bf1-55ba-a8ae-29e7594fc9e2',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name',
    display_name='Murkrow',
    searchable_by=['Murkrow', 'Basic', 'Murkrow'],
    subtypes=['Basic'],
    collector_number=71,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=198,
    abilities=[
        Attack(
            title='Mean Look',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
