from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='69e600db-ead1-5647-91c1-623ffdf62cef',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Honchkrow.Name',
    display_name='Honchkrow',
    searchable_by=['Honchkrow', 'Stage 1', 'Honchkrow'],
    subtypes=['Stage 1'],
    collector_number=79,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name',
    family_id=198,
    abilities=[
        Attack(
            title='Feint Attack',
            game_text="This attack does 30 damage to 1 of your opponent's Pokémon. This damage isn't affected by Weakness, Resistance, or any other effects on that Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Raven's Claw",
            game_text="This attack does 10 more damage for each damage counter on all of your opponent's Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
