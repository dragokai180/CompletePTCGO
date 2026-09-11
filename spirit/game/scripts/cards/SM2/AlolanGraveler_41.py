from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d815f069-197f-5be0-a50d-a3c08bd7c4e0',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGraveler.Name',
    display_name='Alolan Graveler',
    searchable_by=['Alolan Graveler', 'Stage 1', 'AlolanGraveler'],
    subtypes=['Stage 1'],
    collector_number=41,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGeodude.Name',
    family_id=74,
    abilities=[
        Attack(
            title='Thunder Punch',
            game_text='Flip a coin. If heads, this attack does 20 more damage. If tails, this Pokémon does 20 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Electrobullet',
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
