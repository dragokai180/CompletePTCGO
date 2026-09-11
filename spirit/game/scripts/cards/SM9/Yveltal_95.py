from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='572e28e3-c5da-5734-b830-244e831fb88e',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Yveltal.Name',
    display_name='Yveltal',
    searchable_by=['Yveltal', 'Basic', 'Yveltal'],
    subtypes=['Basic'],
    collector_number=95,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=717,
    abilities=[
        Attack(
            title='Derail',
            game_text="Discard a Special Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Clutch',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
