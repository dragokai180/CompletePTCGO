from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6ee81d3e-c327-561f-8ec1-1dbc28a14b4d',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Aerodactyl.Name',
    display_name='Aerodactyl',
    searchable_by=['Aerodactyl', 'Stage 1', 'Aerodactyl'],
    subtypes=['Stage 1'],
    collector_number=130,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.UnidentifiedFossil.Name',
    family_id=142,
    abilities=[
        Attack(
            title='Supersonic',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Fossil Fangs',
            game_text="If you don't have any Pokémon-GX or Pokémon-EX on your Bench, this attack does 90 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
