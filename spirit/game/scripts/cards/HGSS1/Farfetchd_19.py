from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a8f85ba3-9ce8-5733-a02c-a47a36a473ce',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Farfetchd.Name',
    display_name="Farfetch'd",
    searchable_by=["Farfetch'd", 'Basic', 'Farfetchd'],
    subtypes=['Basic'],
    collector_number=19,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=83,
    abilities=[
        Attack(
            title='Collect',
            game_text='Draw 2 cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Spin Turn',
            game_text="Switch Farfetch'd with 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
