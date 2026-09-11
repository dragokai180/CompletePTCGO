from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b231c794-64fc-50fc-bab7-7d5da60f6b04',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tyrantrum.Name',
    display_name='Tyrantrum',
    searchable_by=['Tyrantrum', 'Stage 2', 'Tyrantrum'],
    subtypes=['Stage 2'],
    collector_number=69,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tyrunt.Name',
    family_id=696,
    abilities=[
        Ability(
            title='Tyrannical Heart',
            game_text="As long as you don't have more Pokémon in play than your opponent, this Pokémon's attacks do 60 more damage (before applying Weakness and Resistance), and it takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=standard_passive("As long as you don't have more Pokémon in play than your opponent, this Pokémon's attacks do 60 more damage (before applying Weakness and Resistance), and it takes 30 less damage from attacks (after applying Weakness and Resistance)."),
        ),
        Attack(
            title='Crunch',
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
