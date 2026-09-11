from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cb649efd-b3e8-5cba-84b3-8021a824aca4',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name',
    display_name='Primeape',
    searchable_by=['Primeape', 'Stage 1', 'Primeape'],
    subtypes=['Stage 1'],
    collector_number=22,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name',
    family_id=56,
    abilities=[
        Attack(
            title='Low Kick',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title='Bebop Punch',
            game_text="Choose 1 of your opponent's Pokémon. Flip a coin until you get tails. This attack does 50 damage times the number of heads to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 2},
            effect=standard_attack,
        ),
    ],
)
