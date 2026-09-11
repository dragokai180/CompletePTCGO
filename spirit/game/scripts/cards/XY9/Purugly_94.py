from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c87741d2-941e-5310-a988-100bc8c475ba',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Purugly.Name',
    display_name='Purugly',
    searchable_by=['Purugly', 'Stage 1', 'Purugly'],
    subtypes=['Stage 1'],
    collector_number=94,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Glameow.Name',
    family_id=431,
    abilities=[
        Attack(
            title='Slash',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title='Nyan Press',
            game_text="Flip a coin. If heads, this attack does 40 more damage. If tails, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
