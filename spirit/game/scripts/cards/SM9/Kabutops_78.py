from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='baad5460-b97e-51be-8cae-bb0f0b0bcf3f',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kabutops.Name',
    display_name='Kabutops',
    searchable_by=['Kabutops', 'Stage 2', 'Kabutops'],
    subtypes=['Stage 2'],
    collector_number=78,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name',
    family_id=140,
    abilities=[
        Ability(
            title='Fossilized Memories',
            game_text="As long as this Pokémon is your Active Pokémon, your opponent can't play any Supporter cards from their hand.",
            passive=standard_passive("As long as this Pokémon is your Active Pokémon, your opponent can't play any Supporter cards from their hand."),
        ),
        Attack(
            title='Rock Slide',
            game_text="This attack does 20 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
