from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ca3c85e6-4140-5670-ab3b-8544ba46201b',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Blissey.Name',
    display_name='Blissey',
    searchable_by=['Blissey', 'Stage 1', 'Prime', 'Blissey'],
    subtypes=['Stage 1', 'Prime'],
    collector_number=106,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.RarePrime,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name',
    family_id=113,
    abilities=[
        Ability(
            title='Blissful Nurse',
            game_text='Once during your turn, when you play Blissey from your hand to evolve 1 of your Pokémon, you may remove all damage counters from all of your Pokémon. If you do, discard all Energy attached to those Pokémon that had any damage counters on them.',
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Strength',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)
