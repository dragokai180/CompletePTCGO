from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7538363f-aefc-5b7e-9c14-b81e792a3b2b',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Krookodile.Name',
    display_name='Krookodile',
    searchable_by=['Krookodile', 'Stage 2', 'Krookodile'],
    subtypes=['Stage 2'],
    collector_number=116,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Rare,
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
            title='Chomp Chomp Panic',
            game_text="This attack does 50 damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Crunch',
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
