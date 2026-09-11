from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4c5927b6-8e19-5a89-9170-aa50ec21ba30',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Krookodile.Name',
    display_name='Krookodile',
    searchable_by=['Krookodile', 'Stage 2', 'Krookodile'],
    subtypes=['Stage 2'],
    collector_number=85,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name',
    family_id=551,
    abilities=[
        Attack(
            title='False Accusation',
            game_text="This attack does 20 more damage for each card in your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Obsidian Fang',
            game_text="Before doing damage, discard all Pokémon Tool cards from your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
