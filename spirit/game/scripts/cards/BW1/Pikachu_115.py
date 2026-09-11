from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.pokemon import is_lightning_energy
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="f8adbbbe-efd6-5f14-aa09-652be8bbb7aa",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu","Basic","Pikachu"],
    subtypes=["Basic"],
    collector_number=115,
    set_code="BW1",
    rarity=Rarities.RareSecret,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Energize",
            game_text="Attach a Lightning Energy from your discard pile to this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=attach_from_discard(
                predicate=is_lightning_energy, count=1, target="self",
                prompt="Choose a Lightning Energy card to attach.",
            ),
        ),
        Attack(
            title="Thunderbolt",
            game_text="Discard all Energy attached to this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=bw_legacy_attack,
        ),
    ],
)
