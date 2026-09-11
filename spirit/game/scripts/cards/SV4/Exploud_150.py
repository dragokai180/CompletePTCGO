from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9eb98f2f-6ba2-5f0e-90d0-c0317ba5fc34',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Exploud.Name',
    display_name='Exploud',
    searchable_by=['Exploud', 'Stage 2', 'Exploud'],
    subtypes=['Stage 2'],
    collector_number=150,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Loudred.Name',
    family_id=293,
    abilities=[
        Attack(
            title='Sudden Shout',
            game_text="Discard your opponent's Active Pokémon and all attached cards. If this Pokémon didn't evolve from Loudred during this turn, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Headbang',
            cost={PokemonTypes.COLORLESS: 3},
            damage=140,
        ),
    ],
)
