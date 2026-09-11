from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e55545ab-1228-58ac-a398-37ba59d4b75f',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Oranguru.Name',
    display_name='Oranguru',
    searchable_by=['Oranguru', 'Basic', 'Oranguru'],
    subtypes=['Basic'],
    collector_number=94,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=765,
    abilities=[
        Attack(
            title="Plotter's Command",
            game_text="Choose 1 of your opponent's Active Pokémon's attacks. During your opponent's next turn, that Pokémon can't use that attack.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
            locks_next_turn=True,
        ),
        Attack(
            title='Super Psy Bolt',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
