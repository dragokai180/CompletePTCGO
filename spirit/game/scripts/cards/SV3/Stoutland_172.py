from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='16dcf8ec-f180-5240-af91-f20914d5e64e',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Stoutland.Name',
    display_name='Stoutland',
    searchable_by=['Stoutland', 'Stage 2', 'Stoutland'],
    subtypes=['Stage 2'],
    collector_number=172,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name',
    family_id=506,
    abilities=[
        Attack(
            title='Chomp Chomp Panic',
            game_text="This attack does 50 damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Sharp Fang',
            cost={PokemonTypes.COLORLESS: 3},
            damage=140,
        ),
    ],
)
