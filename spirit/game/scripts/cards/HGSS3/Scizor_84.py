from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='941d228a-4942-578f-846a-1688d32555dd',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scizor.Name',
    display_name='Scizor',
    searchable_by=['Scizor', 'Stage 1', 'Prime', 'Scizor'],
    subtypes=['Stage 1', 'Prime'],
    collector_number=84,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.RarePrime,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name',
    family_id=123,
    abilities=[
        Ability(
            title='Red Armor',
            game_text="Prevent all damage done to Scizor by attacks from your opponent's Pokémon that have any Special Energy cards attached to them.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive("Prevent all damage done to Scizor by attacks from your opponent's Pokémon that have any Special Energy cards attached to them."),
        ),
        Attack(
            title='Metal Scissors',
            game_text='Does 30 damage plus 20 more damage for each Metal Energy attached to Scizor.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
