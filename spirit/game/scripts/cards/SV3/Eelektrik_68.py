from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d648244e-ee3f-5459-9a67-4ce662a8bb7d',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name',
    display_name='Eelektrik',
    searchable_by=['Eelektrik', 'Stage 1', 'Eelektrik'],
    subtypes=['Stage 1'],
    collector_number=68,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name',
    family_id=602,
    abilities=[
        Attack(
            title='Volt Wave',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Electric Ball',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
