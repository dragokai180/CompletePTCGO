from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='47661a21-5fae-5168-b0f0-caf7f3b3aeb4',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nacli.Name',
    display_name='Nacli',
    searchable_by=['Nacli', 'Basic', 'Nacli'],
    subtypes=['Basic'],
    collector_number=102,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=932,
    abilities=[
        Attack(
            title='Corner',
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
