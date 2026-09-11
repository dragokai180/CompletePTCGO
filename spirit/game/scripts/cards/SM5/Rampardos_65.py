from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='11f0b89a-1a36-56bf-b13e-d0e0b89868f1',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rampardos.Name',
    display_name='Rampardos',
    searchable_by=['Rampardos', 'Stage 2', 'Rampardos'],
    subtypes=['Stage 2'],
    collector_number=65,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cranidos.Name',
    family_id=408,
    abilities=[
        Attack(
            title='Clean Hit',
            game_text="If your opponent's Active Pokémon is an Evolution Pokémon, this attack does 60 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Wild Crash',
            game_text="If your opponent's Active Pokémon is a Basic Pokémon, it is Knocked Out.",
            cost={PokemonTypes.FIGHTING: 3},
            effect=standard_attack,
        ),
    ],
)
