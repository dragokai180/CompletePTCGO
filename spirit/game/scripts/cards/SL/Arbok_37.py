from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='76406781-67e0-50fe-b482-8a6c027d4d41',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Arbok.Name',
    display_name='Arbok',
    searchable_by=['Arbok', 'Stage 1', 'Arbok'],
    subtypes=['Stage 1'],
    collector_number=37,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name',
    family_id=23,
    abilities=[
        Ability(
            title='Intimidating Pattern',
            game_text="As long as this Pokémon is your Active Pokémon, your opponent's Active Pokémon's attacks do 30 less damage (before applying Weakness and Resistance).",
            passive=standard_passive("As long as this Pokémon is your Active Pokémon, your opponent's Active Pokémon's attacks do 30 less damage (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Venomous Fang',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
