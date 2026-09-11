from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e094e243-4949-592a-a96f-5ff3495b3ada',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Aerodactyl.Name',
    display_name='Aerodactyl',
    searchable_by=['Aerodactyl', 'Restored', 'Aerodactyl'],
    subtypes=['Restored'],
    collector_number=76,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.RESTORED,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.OldAmberAerodactyl.Name',
    family_id=142,
    abilities=[
        Attack(
            title='Bite',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Jet Draft',
            game_text="Discard a Special Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
