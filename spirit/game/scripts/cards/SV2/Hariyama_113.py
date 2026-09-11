from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3088714e-2d97-5bb8-9468-1b1aadc14ec9',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hariyama.Name',
    display_name='Hariyama',
    searchable_by=['Hariyama', 'Stage 1', 'Hariyama'],
    subtypes=['Stage 1'],
    collector_number=113,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name',
    family_id=296,
    abilities=[
        Ability(
            title='Arm Thrust Practice',
            game_text="All of your Pokémon take 10 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance).",
            passive=standard_passive("All of your Pokémon take 10 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance)."),
        ),
        Attack(
            title='Rocket Slap',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)
